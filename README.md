
# Training-Devops

This repo contains the details about completed/ongoing tasks as part of devOps training(RD-2020 batch)

 1. ### Azure AZ 900 certification
    - Following the Microsoft learning path for Azure Fundamentals from **[here](https://docs.microsoft.com/en-us/learn/paths/azure-fundamentals/)**.  **Completed**
    - Practicing questions from AZ 900 dumps.
<br/>

 2. ### Jenkins tasks
    -  Created a virtual machine on azure and installed Jenkins on it. **[Screenshots](https://github.com/sachinshrma/Training-Devops/blob/master/Jenkins/Docs/InstallJenkins.pdf)**
    - Forked a java project and added pipeline script. **[View](https://github.com/sachinshrma/Training-Devops/blob/master/Jenkins/JenkinsJob/Jenkinsfile)**
    - Executed Build, Test and Deploy stages, and deployed the artifacts on mavenrepo. **[Screenshots](https://github.com/sachinshrma/Training-Devops/blob/master/Jenkins/Docs/DeployPipeline.pdf)**    
    - Added an ubuntu slave node to Jenkins sever. **[Screenshots](https://github.com/sachinshrma/Training-Devops/blob/master/Jenkins/Docs/SlaveNode.pdf)**    
<br/>

 3. ### Terraform Learning
    - Gained knowledge on terraform.
    - Written **AvailabilitySet** and **Shared Image Gallery** module for the usecase. **[View](https://github.com/sachinshrma/Training-Devops/tree/master/Terraform/Modules/Compute)**
<br/>

 4. ### Python Learning
    - Attending python training which is ongoing and practicing the topics.
    - Wrote a python script for provisioning a virtual machine on Azure. **[View](https://github.com/sachinshrma/Training-Devops/tree/master/Python/Azure/Compute)**
 <br/>
 
 5. ### CI/CD usecase **[link](https://github.com/sachinshrma/spring-petclinic)**
    - Created CI pipeline which builds and test the spring webapp.
    - Added code analysis stage which analyses the java code using sonarcloud.
    - Added Containerization stage which containerizes the application using docker and pushes the image to docker hub.
    - Added deploy stage which provisions a vm on azure and then run the application container on that vm.
    - Added Email notification step which sends the build status to email after every build.
    - Deployed multi-container app on Azure web apps.
    - Created Kubernetes cluster on Aks and deployed spring application and mysql pods on that. Also exposed the application pods to internet using loadbalancer.

