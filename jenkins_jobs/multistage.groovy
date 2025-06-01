def sharedVar = 'sharedVar'


pipeline {
    agent any 

    environment{
        GLOBAL_VAR = 'inti'
        SOME_VAR = 1

    }
    stages{
        stage('get token'){
            steps {
                script{
                    echo "stage 1 Переменная GLOBAL_VAR до изменения ${env.GLOBAL_VAR}"
                    echo "stage 1 Переменная sharedVar до изменения ${sharedVar}"
                    env.GLOBAL_VAR = 'Hello from Stage 1'
                    sharedVar = "Data from Stage 1"
                }
            }
        }
        stage('use token'){
            steps {
                script{
                    echo "Значение env.GLOBAL_VAR: ${env.GLOBAL_VAR}"
                    println(env.SOME_VAR)
                    echo "Значение sharedVar: ${sharedVar}"
                }
            }

        }
    }           
 
}
