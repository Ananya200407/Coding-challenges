class RoleBuilder:
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    @staticmethod
    def get_role_description(role_id):
        if role_id >= 1 and role_id <= 4:
            return RoleBuilder.ROLES[int(role_id)]
        return "UNDEFINED"
