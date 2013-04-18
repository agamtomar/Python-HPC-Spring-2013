# Configuration file for ipcluster.
import os
import sys 

c = get_config()
print c
c.LocalControllerLauncher.controller_args = ['--log-to-file', '--log-level=20', "--ip='*'"]
c.IPClusterEngines.engine_launcher_class = 'SSH'
c.SSHEngineLauncher.remote_profile_dir = u'.ipython/profile_ssh'
c.SSHEngineLauncher.to_send = []
c.SSHEngineLauncher.to_fetch = []
c.SSHEngineLauncher.ssh_args = ['-t']

print c

c.IPClusterStart.n = 12

print c.IPClusterStart.n

c.SSHEngineSetLauncher.engines  = {}
filename = os.environ['PBS_NODEFILE']
with open(filename,'r') as file:
    for line in file:
        node_name = line.split()[0]
        if node_name not in c.SSHEngineSetLauncher.engines:
            c.SSHEngineSetLauncher.engines[node_name] = c.IPClusterStart.n

c.SSHEngineLauncher.engine_args = []
c.IPClusterStart.work_dir = os.environ['PBS_O_WORKDIR']
c.IPClusterStart.delay = 1.0
c.IPClusterStart.log_to_file = True
c.IPClusterStart.early_shutdown = 10
c.IPClusterStart.clean_logs = True

