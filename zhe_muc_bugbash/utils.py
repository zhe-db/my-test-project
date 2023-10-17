"""This module contains utils shared between different notebooks"""


def get_deployed_model_alias_for_env(env):
    """Get the registered model alias under which the latest deployed model version can be found
    for the current environment
    :param env: Current environment
    :return: Model alias
    """
    # For a model registered in Unity Catalog to be served, it needs have either a "Champion" or "Challenger" alias.
    # (https://learn.microsoft.com/azure/databricks/applications/machine-learning/manage-model-lifecycle/index#transition-a-model-stage).
    # For models in dev and staging environments, we assign the model version the "Challenger" alias, and in prod we assign the model version 
    # the "Champion" alias.
    _MODEL_STAGE_FOR_ENV = {
        "dev": "Challenger",
        "staging": "Challenger",
        "prod": "Champion",
        "test": "Challenger",
    }
    return _MODEL_STAGE_FOR_ENV[env]
