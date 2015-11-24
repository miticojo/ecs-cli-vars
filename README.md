AWS ECS CLI VARS
================
This script substitutes ${VARIABLE} in Docker compose file with OS environment variables.
It has been developed for [**ecs-cli compose**](https://github.com/aws/amazon-ecs-cli) function, that actually doesn't implement that feature ([improvement request already opened](https://github.com/aws/amazon-ecs-cli/issues/28)).

Usage example
-------------
Set single variables:
> export RELEASE_VERSION=1.0.1

or multiple variables in a properties file:
> source ./variables_file.properties

Docker-compose file (for this example):

    db:
      image: "postgres:${RELEASE_VERSION}"

Run **ecs-cli-vars.py** with "-f " parameter followed by docker-compose.yml file
> python  ***ecs-cli-vars.py -f  docker-compose.yml***

Results:

    db:
      image: "postgres:1.0.1"

Finally for your CI scripts:
> python  ***ecs-cli-vars.py -f  docker-compose.yml > docker-compose-prod.yml***

