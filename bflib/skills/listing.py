skill_listing = set()
skills_by_name = {}


def register(skill):
    skill_listing.add(skill)
    skills_by_name[skill.name] = skill

    return skill


def get_skill_by_name(name):
    return skills_by_name.get(name)
