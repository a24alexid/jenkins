pipeline {
    agent {
        docker { 
            image 'python:3'  // Aquí especificamos que se usará a imaxe de Docker 'python:3'
            args '-u root'    // Facultativo: pódese engadir se queres executar como root
        }
    }

    environment {
        // Definimos o nome do entorno virtual que se vai crear
        VENV_DIR = '.venv'
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                // Clonamos o repositorio especificando a rama 'main'
                git branch: 'main', url: 'https://github.com/a24alexid/jenkins.git'
            }
        }

        stage('Configurar Entorno Virtual') {
            steps {
                script {
                    // Se non existe o entorno virtual, créao
                    if (!fileExists(VENV_DIR)) {
                        sh 'python3 -m venv ${VENV_DIR}'
                    }
                    // Activamos o entorno virtual
                    sh '. ${VENV_DIR}/bin/activate'
                }
            }
        }

        stage('Instalar Dependencias') {
            steps {
                script {
                    // Instalamos as dependencias (por exemplo, as do requirements.txt)
                    sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Executar Test') {
            steps {
                script {
                    // Executamos os tests de Python (usando pytest ou unittest, dependendo do que utilices)
                    sh '. ${VENV_DIR}/bin/activate && pytest'
                }
            }
        }
    }

    post {
        always {
            // Elimina o entorno virtual para limpar despois da execución
            sh 'rm -rf ${VENV_DIR}'
        }

        success {
            echo 'Os tests executáronse correctamente.'
        }

        failure {
            echo 'Produciuse un erro na execución dos tests.'
        }
    }
}
