from gym.envs.registration import register


register(
    id='Waf-v0',
    entry_point='lib.gym.envs.wafEnv:WafEnv_v0',
)



