# backend/recommender.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def build_corpus_docs(internships):
    # create a combined text for each internship
    docs = []
    ids = []
    for it in internships:
        parts = [
            it.get("title",""),
            it.get("org",""),
            it.get("description",""),
            " ".join(it.get("required_skills", [])),
            it.get("sector",""),
            it.get("location","")
        ]
        docs.append(" ".join(parts))
        ids.append(it.get("_id"))
    return docs, ids

def recommend_topk(profile_text, candidate_skills, internships, top_k=5, w_text=0.6, w_skill=0.4):
    """
    Combine TF-IDF cosine similarity on text and skill-match ratio.
    Returns list of {internship, score, matched_skills}
    """
    docs, ids = build_corpus_docs(internships)
    if len(docs) == 0:
        return []

    vectorizer = TfidfVectorizer(stop_words='english', max_features=2000)
    X = vectorizer.fit_transform(docs)            # internships matrix
    q_vec = vectorizer.transform([profile_text]) # profile vector

    sims = cosine_similarity(q_vec, X).flatten()  # similarity for each internship (0..1)

    results = []
    for idx, it in enumerate(internships):
        req_skills = [s.lower() for s in it.get("required_skills", [])]
        cand_skills = [s.lower() for s in (candidate_skills or [])]
        matched = [s for s in req_skills if s in cand_skills]
        skill_ratio = (len(matched) / len(req_skills)) if len(req_skills)>0 else 0.0

        text_score = float(sims[idx])  # 0..1
        combined = w_text*text_score + w_skill*skill_ratio  # 0..1 approx
        score = round(combined * 100, 2)  # scale to 0..100

        results.append({
            "internship": it,
            "score": score,
            "matched_skills": matched
        })

    results_sorted = sorted(results, key=lambda x: x["score"], reverse=True)
    return results_sorted[:top_k]
