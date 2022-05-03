import json

__data = []


def load_candidates_from_json(path):
    global __data
    with open("canditates.json","r", encoding="utf8") as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    for candidate in __data:
        if candidate["id"] == candidate_id:
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"]
            }
    return {"not_found": "Ничего не найдено :("}


def get_candidates_by_name(candidate_name):
    return [candidate for candidate in __data if candidate_name.lower() in candidate["name"].lower()]


def get_candidates_by_skill(skill_name):
    candidates_skill = []
    for candidate in __data:
        skills = candidate["skills"].lower().split(", ")
        if skill_name in skills:
            candidates_skill.append(candidate)
    return candidates_skill




