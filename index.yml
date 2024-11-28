#!/bin/bash

#export SLS_DEBUG=*
cwd=$(pwd)

echo 'configure npm version'
source $HOME/.nvm/nvm.sh
nvm use v12.22.6

echo 'activate prems'

if [[ $stage == "dev" || $stage == "beta" ]]; then
	aws s3 cp s3://paas-deployment-bucket/artifacts/tkyc-webapp/perfios/prems/tkyc_webapp_aws_dev_beta $HOME/.prems/tkyc_webapp_aws_prems
elif [[ $stage == "test" || $stage == "prod" ]]; then
	aws s3 cp s3://paas-deployment-bucket/artifacts/tkyc-webapp/perfios/prems/tkyc_webapp_aws_test_prod $HOME/.prems/tkyc_webapp_aws_prems
fi

source $HOME/.prems/activate_prem_source.sh
aprem tkyc_webapp_aws_prems
#unset AWS_PROFILE

ln -s /home/ubuntu/tmp/dependencies/node_modules $cwd/node_modules

#source /datadrive/virtualenvs/py3.7/bin/activate
echo 'creating python venv'
cd /home/ubuntu/virtualenvs/
sudo apt install python3.10-venv
#to be used python3.10 from jan17 2024
python3.10 -m venv py3.10
source /home/ubuntu/virtualenvs/py3.10/bin/activate
python3 --version

cd $cwd

echo $list_of_functions
IFS=','
read -ra functions <<< "$list_of_functions"

echo "--------------- Build Started----------------------"
#if condition to deploy list_of_function or all_functions
if [[ -z "$list_of_functions" ]]; then
	sls deploy -s $stage
elif [[ -n "$list_of_functions" ]]; then
	for i in "${functions[@]}"; do
        echo "############ Packaging $i ##############"
    	sls package -s $stage -f "$i"
        echo "############ Deploying $i Function #####"
    	sls deploy -s $stage -f "$i"
    done
fi

# cleanup
echo 'deactivating and deleting venv'
deactivate
rm -rf /home/ubuntu/virtualenvs/venv
#aws cloudformation describe-stacks --stack-name totalkycplus-webapp-dev
