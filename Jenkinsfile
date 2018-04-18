node {
    def scmVars
        stage('Build') {
                echo 'Building..'
        }
        stage('Test') {
                echo 'Testing..'
        }
        stage('Deploy') {

              def environment = "Prod"
              def description = "Deploying this branch"
              def ref = scmVars.GIT_COMMIT
              def owner = "webdog"
              def repo = "jenkinsdays-app"
              def deployURL = "https://api.github.com/repos/${owner}/${repo}/deployments"
              def deployBody = '{"ref": "' + ref +'","environment": "' + environment  +'","description": "' + description + '","required_contexts": []}'



              // Create new Deployment using the GitHub Deployment API
              def response = httpRequest authentication: 'jenkins-temp', httpMode: 'POST', requestBody: deployBody, responseHandle: 'STRING', url: deployURL, validResponseCodes: '100:599'

              if(response.status != 201) {
                  error("Deployment API Create Failed: " + response.status + response.content)
              }

              // Get the ID of the GitHub Deployment just created
              def responseJson = readJSON text: response.content
              def id = responseJson.id
              if(id == "") {
                  error("Could not extract id from Deployment response")
              }

              // Execute Deployment
              def deployStatus = sh returnStatus: true, script: 'echo deploy'

              // Record new Deployment Status based on output
              def result = (deployStatus) ? 'failure' : 'success'
              def deployStatusBody = '{"state": "' + result + '","target_url": "http://github.com/deploymentlogs"}'
              def deployStatusURL = "https://api.github.com/repos/${owner}/${repo}/deployments/${id}/statuses"
              def deployStatusResponse = httpRequest authentication: 'mfilosaPAT', httpMode: 'POST', requestBody: deployStatusBody , responseHandle: 'STRING', url: deployStatusURL
              if(deployStatusResponse.status != 201) {
                error("Deployment Status API Update Failed: " + deployStatusResponse.status)
                }
        }        
}
