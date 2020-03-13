pipeline {
    agent {
      node { 
        label 'py-coad'
	      
      }
    }
    
    options {
      buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
      disableConcurrentBuilds()              
    }
    
        
    stages {
	 stage('BD') {
        agent {
          label 'master'
        }  
     steps {
        script {
          CONTAINER_ID = sh (
          script: 'docker ps -q --filter "name=coad-db"',
          returnStdout: true
          ).trim()
           if (CONTAINER_ID) {
            sh "echo nome é: ${CONTAINER_ID}"
            sh "docker rm -f ${CONTAINER_ID}"
            sh 'docker run -d --rm --cap-add SYS_TIME --name coad-db --network python-network -p 5432 -e TZ="America/Sao_Paulo" -e POSTGRES_DB=coad -e POSTGRES_PASSWORD=adminadmin -e POSTGRES_USER=postgres postgres:11-alpine'
        } else {
        //    sh "echo nome é: ${CONTAINER_ID}"
            sh 'docker run -d --rm --cap-add SYS_TIME --name coad-db --network python-network -p 5432 -e TZ="America/Sao_Paulo" -e POSTGRES_DB=coad -e POSTGRES_PASSWORD=adminadmin -e POSTGRES_USER=postgres postgres:11-alpine'
       }
        }

        }
      }
	
	
	
      stage('CheckOut') {
        steps {
          checkout scm		
        }
      }
      
       stage('Setup ambiente') {
         steps {
               
           sh 'mv env_sample .env'
           sh 'pip install --user -r requirements/local.txt'    
        }
      } 
        
             
      stage('Analise Codigo') {
          when {
                branch 'homolog'
          }
         steps {
           sh 'sonar-scanner \
                -Dsonar.projectKey=SME-Contratos-BackEnd \
                -Dsonar.sources=. \
                -Dsonar.exclusions=htmlcov \
                -Dsonar.host.url=http://automation.educacao.intranet:9000 \
                -Dsonar.login=1426bd14e5f9a2d6a3e5af46ba81d196b936e1ce \
                -Dsonar.language=py \
                -Dsonar.sourceEncoding=UTF-8'
         }
       }
      
       stage('Testes') {
         steps {
           sh "echo executar testes"
           //sh 'pytest'
           //sh 'flake8'
           //sh 'ls -la htmlcov'
         }
          
         
       }
        
      stage('Deploy DEV') {
            when {
                branch 'develop'
            }
            steps {
                 
                 sh 'echo Deploying desenvolvimento'
                
                // Start JOB Rundeck para build das imagens Docker e push SME Registry
      
          script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
              jobId: "d1b79a24-e2d3-47e4-936f-3bcc8970986f",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
           }
                
       //Start JOB Rundeck para update de deploy Kubernetes 
         
         script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
              jobId: "819496ff-aaf3-480c-b871-ad0d1a1f3c54",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
           }
      
       
            }
        }
        
        stage('Deploy QA') {
            when {
                branch 'develop'
            }
            steps {
                sh 'echo Deploying QA'
            }
        }
      
      stage('Deploy homologacao') {
            when {
                branch 'homolog'
            }
            steps {
                 timeout(time: 24, unit: "HOURS") {
               
                 telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME} - Requer uma aprovação para deploy !!!\nBranch name: ${GIT_BRANCH}\n Consulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)\n")
                 input message: 'Deseja realizar o deploy?', ok: 'SIM', submitter: 'ebufiano, marcos_nastri,alessandro_fernandes'
            }
                 sh 'echo Deploying homologacao'
                
                // Start JOB Rundeck para build das imagens Docker e push SME Registry
      
          script {
           step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
                             
              //JOB DE BUILD
              jobId: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
           }
                
       //Start JOB Rundeck para update de imagens no host homologação 
         
         script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
              jobId: "xxxxxxxxxxxxxxxxxxxxxxxx",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
           }
      
       
            }
        }
		
    // LIMPA AMBIENTE CRIADO
    stage('Limpeza ambiente') {
        agent {
          node {
            //utiliza master  
            label 'master'
          }
        }
        steps {
          sh 'docker rm -f coad-db'   
        }
        
      }
     
}

    
post {
        always {
            
            echo 'One way or another, I have finished'
            
            
        }
        success {
           
            telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME} - Esta ok !!!\n Consulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)\n\n Uma nova versão da aplicação esta disponivel!!!")
        }
        unstable {
           
            telegramSend("O Build ${BUILD_DISPLAY_NAME} <${env.BUILD_URL}> - Esta instavel ...\nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
        }
        failure {
            
             telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME}  - Quebrou. \nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
        }
        changed {
             
               echo 'Things were different before...'
            
        }
       aborted {
             
             telegramSend("O Build ${BUILD_DISPLAY_NAME} - Foi abortado.\nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
        }
    }
}
