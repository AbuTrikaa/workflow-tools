# Workflow Tools

Small collection of helper scripts and utilities used to prepare a workspace, package artifacts, and generate simple reports. Intended for onboarding and light automation tasks.

## Quick start

```bash
# clone repo
git clone --recursive https://github.com/AbuTrikaa/workflow-tools.git
cd workflow-tools

# set up workspace
./scripts/setup_workspace.sh

# generate a sample report
python3 tools/report_generator.py examples/sample_config.yml

# cleanup when done
./scripts/cleanup_workspace.sh