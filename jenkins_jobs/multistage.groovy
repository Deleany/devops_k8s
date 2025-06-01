def sharedVar = 'sharedVar'

pipeline {
    agent any

    environment {
        GLOBAL_VAR = 'initial'
    }
    stages {
        stage('get token') {
            steps {
                script {
                    echo "stage 1 Переменная GLOBAL_VAR до изменения ${env.GLOBAL_VAR}"
                    echo "stage 1 Переменная sharedVar до изменения ${sharedVar}"
                    env.GLOBAL_VAR = 'changed in Stage 1'
                    sharedVar = 'changed Data from Stage 1'
                }
            }
        }
        stage('use token') {
            steps {
                script {
                    echo "Значение env.GLOBAL_VAR: ${env.GLOBAL_VAR}"
                    echo "Значение GLOBAL_VAR: ${GLOBAL_VAR}"
                    echo "Значение sharedVar: ${sharedVar}"
                }
            }
        }
    }
}
