# Docker
i alias d as docker
## official tutorial
https://docs.docker.com/get-started/part2/
## command
`docker run hello-world` test the basic function of docker
`docker version` show the version of docker
`docker --version` show version
`d info` show details
`docker search ubuntu`
`docker pull ubuntu`
`d image ls` show the installed images in pc
`d container ls --all` all produced container in sys


`d ps -a`
`d start -a [id]`
`d attach [id]`
`d kill [id]`
`d start --help`
`d commit [id] [name:version]`
## run ubuntu
https://my.oschina.net/wuxinshui/blog/847559
https://my.oschina.net/u/146514/blog/512025
1. `d search ubuntu`
2. `d pull ubutun`
3. `d images `
4. `docker run -t -i ubuntu:latest //bin/bash `
5. `apt-get update `
6. `apt-get install openssh-server openssh-client `
7. `passwd`
8. `vim /etc/ssh/sshd_config` `PermitRootLogin yes` `service ssh start`
8. `d ps -l` `d ps -a`
9. `d commit [id] ubuntu:ssh`
10. `d run -d -p 122:22 ubuntu:ssh /usr/sbin/sshd -D`
11. `ssh -p 122 root@192.168.31.232`

- `d kill 0605`
- `d start 0605`
- `d ps -a`
## help file
Usage:	docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/Users/andrew/.docker")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal")
                           (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "/Users/andrew/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/Users/andrew/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/Users/andrew/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  config      Manage Docker configs
  container   Manage containers
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes
