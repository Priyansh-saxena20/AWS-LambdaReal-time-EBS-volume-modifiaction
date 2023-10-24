# AWS-Lambda-Real-time-EBS-volume-modifiaction
This is the AWS Lambda code to modified EBS volume from type GP2 to GP3 on the Real time,
In this i have created a event Bus where a EBS volume Creation Event will trigger a lambda function which will convert the EBS vloume to GP3 type automatically.
In the AWS lambda , i have created a python function which will first get the ebs volume arn id using string split method then this will return the volume id to boto3 client which will modify ebs volume 


## Here are some of the screenshots for the refrence
![Screenshot (1002)](https://github.com/Priyansh-saxena20/AWS-LambdaReal-time-EBS-volume-modifiaction/assets/111503326/6de1267c-fb76-4324-9db1-04eddd0f90d4)

![Screenshot (1003)](https://github.com/Priyansh-saxena20/AWS-LambdaReal-time-EBS-volume-modifiaction/assets/111503326/1c470bf3-ac0b-4718-9605-67b2103914cd)
![Screenshot (1004)](https://github.com/Priyansh-saxena20/AWS-LambdaReal-time-EBS-volume-modifiaction/assets/111503326/0e5c8e0a-e295-4936-81f5-b1b7c5da580c)
![Screenshot (1005)](https://github.com/Priyansh-saxena20/AWS-LambdaReal-time-EBS-volume-modifiaction/assets/111503326/2d0eaca6-a54f-4432-a9f3-a28df8156543)
![Screenshot (1006)](https://github.com/Priyansh-saxena20/AWS-LambdaReal-time-EBS-volume-modifiaction/assets/111503326/b9a199cd-586c-4923-b9a3-4452f09e5a3e)
![Screenshot (1007)](https://github.com/Priyansh-saxena20/AWS-LambdaReal-time-EBS-volume-modifiaction/assets/111503326/77ce0ea7-509b-4918-96d2-43133ff872bc)
![Screenshot (1008)](https://github.com/Priyansh-saxena20/AWS-LambdaReal-time-EBS-volume-modifiaction/assets/111503326/523993a1-4a0e-405e-a2e4-353eccdc34ab)
