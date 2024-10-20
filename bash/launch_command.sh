# This is the command frontend to launcher.sh
# This is not supposed to be a file, but a symbolic link to launcher.sh where you can pass parameters
# needed for the launcher.sh or any programs called by the launcher.sh script (Python scripts).
./launcher.sh

#
# Pattern used for launching Python scripts setting environments prior to it being called.
# Typically makes it possible to "hide" parameters/settings as environment variables and other
# info that the Python script needs to run, shielding the user from these details.
#
