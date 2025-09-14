pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/enesum6/Number-Guessing-Game.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Build aşaması (örnek: tahmin yapılabilir)"'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline tamamlandı.'
        }
    }
}
