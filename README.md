# ☁️ AWS Cloud Portfolio

This project demonstrates a full-featured **AWS cloud portfolio** consisting of:

- ✅ **Static Website** hosted on S3 + CloudFront  
- ✅ **Serverless To-Do API** using AWS Lambda + API Gateway + DynamoDB  
- ✅ **CI/CD Deployment to EC2** using GitHub Actions + AWS CodeDeploy

![Deploy Status](https://github.com/Sundin-I/cloud-portfolio-713/actions/workflows/deploy.yml/badge.svg)

---

## 🌐 1. Static Website (Frontend)

- **Hosted on**: Amazon S3 (static site hosting)  
- **Accelerated with**: Amazon CloudFront (CDN + HTTPS)  
- **Live URL**:  
  [https://d7q2iujpllljr.cloudfront.net](https://d7q2iujpllljr.cloudfront.net)  
  *(S3 origin: [`sundin-portfoliobucket713.s3-website.us-east-2.amazonaws.com`](http://sundin-portfoliobucket713.s3-website.us-east-2.amazonaws.com))*
### 🔍 Preview

![Static Site](IMG_S2713.png)


### Features:
- HTML/CSS portfolio showcasing cloud projects  
- Automatically synced via AWS CLI (`aws s3 sync`)
Licensed under MIT – contributions welcome on GitHub

---

## 🧠 2. Serverless API (To-Do App)

- **Built with**: Python (or Node.js) Lambda functions  
- **Accessed through**: Amazon API Gateway  
- **Data stored in**: Amazon DynamoDB

### CRUD Endpoints:
- `GET /tasks` → Fetch all tasks  
- `POST /tasks` → Create a new task  
- `PUT /tasks/{id}` → Update a task  
- `DELETE /tasks/{id}` → Delete a task
Licensed under MIT – contributions welcome on GitHub

## 🚀 3. CI/CD Pipeline (GitHub Actions → AWS CodeDeploy → EC2)

This project includes a fully automated CI/CD pipeline that deploys updated code from GitHub to an EC2 instance using AWS CodeDeploy.

### 🛠️ Stack:

- **Source Control**: GitHub  
- **CI/CD Engine**: GitHub Actions  
- **Deployment Service**: AWS CodeDeploy  
- **Target Environment**: Amazon EC2 (Ubuntu)
Licensed under MIT – contributions welcome on GitHub

---

### 🔁 Deployment Flow

1. Developer pushes code to `main` branch  
2. GitHub Actions triggers `.github/workflows/deploy.yml`  
3. AWS CodeDeploy receives the deployment artifact  
4. CodeDeploy deploys it to the EC2 instance using `appspec.yml`
Licensed under MIT – contributions welcome on GitHub

---

### 📁 Key Files

- `.github/workflows/deploy.yml` – CI/CD pipeline definition  
- `appspec.yml` – Instructions for CodeDeploy on EC2  
- `scripts/` – Shell scripts run during deployment lifecycle

