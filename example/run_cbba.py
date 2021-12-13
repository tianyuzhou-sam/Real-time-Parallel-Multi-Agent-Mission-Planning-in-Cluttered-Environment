#!/usr/bin/env python3
import os
import time
import json
import matplotlib.pyplot as plt
import pathmagic
with pathmagic.context():
    from CBBA import CBBA
    from WorldInfo import WorldInfo
    import HelperLibrary as HelperLibrary


if __name__ == "__main__":
    # a json configuration file
    config_file_name = os.getcwd() + "/example/cbba_config.json"
    # Read the configuration from the json file
    json_file = open(config_file_name)
    config_data = json.load(json_file)

    # create a world, each list is [min, max] coordinates for x,y,z axis
    WorldInfoTest = WorldInfo([-2.0, 2.5], [-1.5, 5.5], [0.0, 20.0])

    # create a list of Agent(s) and Task(s)
    num_agents = 1
    num_tasks = 10
    max_depth = num_tasks
    AgentList, TaskList = HelperLibrary.create_agents_and_tasks_homogeneous(
        num_agents, num_tasks, WorldInfoTest, config_data)

    # create a CBBA solver
    CBBA_solver = CBBA(config_data)

    t_start = time.time()

    # solve, no time window
    path_list, _ = CBBA_solver.solve(AgentList, TaskList, WorldInfoTest, max_depth, time_window_flag=False)

    t_end = time.time()
    t_used = t_end - t_start
    print("Time used [sec]: ", t_used)

    # the output is CBBA_solver.path_list or path_list
    print("bundle_list")
    print(CBBA_solver.bundle_list)
    print("path_list")
    print(path_list)

    # plot without time window
    CBBA_solver.plot_assignment_without_timewindow()
    plt.show()
