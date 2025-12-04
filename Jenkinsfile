pipeline {
    agent any

    environment {
        // Path to Python (optional if python3 is already in PATH)
        PYTHON = "/usr/bin/python3"
        // Name of virtual environment
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                    # Create venv if not exists
                    if [ ! -d "$VENV" ]; then
                        $PYTHON -m venv $VENV
                    fi
                    source $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Script 1') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    python script1.py
                '''
            }
        }

        stage('Run Script 2') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    python script2.py
                '''
            }
        }

        stage('Run Script 3') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    python script3.py
                '''
            }
        }

        stage('Run Script 4') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    python script4.py
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
    }
}
