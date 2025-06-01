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
                    env.GLOBAL_VAR = 'Hello from Stage 1'
                }
            }
        }
        stage('use token'){
            steps {
                script{
                    echo "Значение из Stage 1: ${env.GLOBAL_VAR}"
                    println(env.SOME_VAR)
                }
            }

        }
    }           
 
}
