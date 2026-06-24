Today I'm going to learn how to integrate a CI/CD pipeline.

First, we need to know what's executed inside the .yml file.

So, inside the .yml file, we have on, permission, and jobs.
First, on? This .yml file will contain an event, some of which are push and pull requests that will directly direct to the main/master branch.

Second, permission? Permissions are used to determine the workflow's access rights to the GitHub repository. Since it's read-only, the workflow can only read the repository's contents without making any changes.

Third, jobs? Within a job, it will be executed sequentially, starting with build, which means create. Since this is run in the CI/CD automation terminal, the first job to be executed is to run the runner running on the latest Ubuntu. Then there are steps, which represent the steps that will be executed within that step. There are several, namely run and uses. Run is used to run commands or scripts that we write ourselves in the runner, while uses is used to invoke pre-created GitHub Actions, either by GitHub or the open source community.
