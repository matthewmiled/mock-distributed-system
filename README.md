# mock-distributed-system

```commandline
pipenv run gunicorn -c python:webserver.gunicorn_config webserver.wsgi:app
```

docker build -t test-mock-dist .
docker run -p 8080:8080 test-mock-dist

# TODO

https://aws.amazon.com/getting-started/guides/deploy-webapp-ecs/

https://towardsthecloud.com/amazon-ecs-execute-command-access-container#1_Verify_if_ECS_Exec_is_enabled_on_an_ECS_task

```commandline
aws ecs list-task-definitions
aws ecs list-clusters
```

* Deploy the app as a service to ECS
* Ensure it is running, but won't be accessible - might have logs
* Won't be accessible because it probably won't have a public IP address by default
* Probably need to amend the task definition so it has a public IP and uses an app load balancer
* 

* Deploy the flask app (using gunicorn) to the ec2 instance in our existing ECS cluster
* SSH into ec2 and curl localhost:5000 to confirm its running
  * Can maybe install the ecs-cli, so can view ECS resources via the CLI and therefore tell where this webapp is running etc
* Can then setup NGINX so can access it externally (outside of the instance/cluster)
* Once NGINX setup, should be able to grab IP of instance or pod and paste in a browser


# Debugging

* If we SSH into a task container using

```
aws ecs execute-command --cluster <cluster-name> \
    --task <task-id> \
    --container <container-name> \
    --interactive \
    --command "/bin/sh"
```

* And then grab the private IP address of a running task and curl it `curl 172.31.42.52:8080` - then we get 'Connection Refused'

* But if we curl it from outside the cluster/container - we get 'Connection Timed Out'.

* And if we `curl localhost:8080` from within the container - it succeeds. 

* So the web service is running, it just can't be reached externally. 

* For this, we will need to set up NGINX or load balancer?
  - https://medium.com/@prithvishetty/deploying-multiple-python-3-flask-apps-to-aws-using-nginx-d78e9477f96d

*
