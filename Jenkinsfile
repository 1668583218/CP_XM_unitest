pipeline{
	agent any
    stages{
        stage("test"){
        	steps{
        	bat '''cd scripts
                    python run_html.py'''
        	}
        }
}
}