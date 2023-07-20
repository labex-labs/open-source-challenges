# Cleaning Up

Execute the `docker service rm sleep-app` command on **node1** to remove the service called _myservice_.

```bash
docker service rm sleep-app
```

Execute the `docker ps` command on **node1** to get a list of running containers.

```bash
docker ps
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
044bea1c2277        ubuntu              "sleep infinity"    17 minutes ago      17 minutes ag                           distracted_mayer
```

You can use the `docker kill <CONTAINER ID>` command on **node1** to kill the sleep container we started at the beginning.

```
docker kill yourcontainerid
```

Finally, let's remove node1, node2, and node3 from the Swarm. We can use the `docker swarm leave --force` command to do that.

Lets run `docker swarm leave --force` on **node1**.

```bash
docker swarm leave --force
```

Then, run `docker swarm leave --force` on **node2**.

```.term2
docker swarm leave --force
```

Finally, run `docker swarm leave --force` on **node3**.

```.term3
docker swarm leave --force
```
