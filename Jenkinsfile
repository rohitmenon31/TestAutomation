pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    
                    # Install required modules even without requirements.txt
                    pip install playwright pytest
                    
                    # Install Playwright browsers
                    python -m playwright install
                '''
            }
        }

        stage('Run Script 1') {
            steps {
                sh '''
                    source venv/bin/activate
                    python test1.py
                '''
            }
        }

        stage('Run Script 2') {
            steps {
                sh '''
                    source venv/bin/activate
                    python test2.py
                '''
            }
        }

        stage('Run Script 3') {
            steps {
                sh '''
                    source venv/bin/activate
                    python test3.py
                '''
            }
        }

        stage('Run Script 4') {
            steps {
                sh '''
                    source venv/bin/activate
                    python test4.py
                '''
            }
        }
    }
}
