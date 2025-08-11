# 🤖 Intelligent Document Q&A System: Enterprise RAG Application with AWS Cloud Deployment

[![Build Status](https://github.com/yourusername/intelligent-rag-qa-system/workflows/CI-CD/badge.svg)](https://github.com/yourusername/intelligent-rag-qa-system/actions)
[![AWS](https://img.shields.io/badge/AWS-Cloud%20Native-orange)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)](https://streamlit.io)

## 📖 Project Overview

The **Intelligent Document Q&A System** is a production-ready, enterprise-grade Retrieval-Augmented Generation (RAG) application that enables users to interact with their documents through natural language queries. Built with modern MLOps practices, this system leverages the power of Large Language Models (LLMs) to provide accurate, contextual answers from your document corpus.

### 🌟 Key Features

- **🔍 Smart Document Retrieval**: Advanced semantic search using vector embeddings
- **💬 Natural Language Q&A**: Conversational interface for document querying  
- **☁️ Cloud-Native Architecture**: Fully deployed on AWS with auto-scaling capabilities
- **🔄 MLOps Pipeline**: Complete CI/CD workflow with automated testing and deployment
- **📊 Interactive Web Interface**: User-friendly Streamlit dashboard
- **🐳 Containerized Deployment**: Docker-based deployment for consistency across environments
- **🔐 Enterprise Security**: IAM-based access control and secure API endpoints
- **📈 Production Monitoring**: Built-in logging and performance tracking

### 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   RAG Engine    │    │   AWS Bedrock   │
│   Frontend      │───▶│   (LangChain)   │───▶│      LLM        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Query    │    │  Vector Store   │    │  Generated      │
│   Processing    │    │  & Retrieval    │    │  Response       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- AWS Account with appropriate permissions
- Docker Desktop
- Git
- Conda or Python virtual environment

### 1. Repository Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/intelligent-rag-qa-system.git
cd intelligent-rag-qa-system

# Create and activate virtual environment
conda create -p ragproj1 python==3.10 -y
conda activate ragproj1

# Install dependencies
pip install -r requirements.txt
```

### 2. Project Structure Creation

```bash
# Create the main project structure
mkdir -p SRC/QASystem
touch SRC/__init__.py
touch SRC/QASystem/__init__.py
touch SRC/QASystem/ingestion.py
touch SRC/QASystem/retrievalandgeneration.py
```

Your project structure should look like this:

```
intelligent-rag-qa-system/
├── SRC/
│   ├── __init__.py
│   └── QASystem/
│       ├── __init__.py
│       ├── ingestion.py
│       └── retrievalandgeneration.py
├── .github/
│   └── workflows/
│       └── main.yaml
├── ragproj1/                 # Virtual environment (in .gitignore)
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Configuration & Deployment

### AWS Infrastructure Setup

#### 1. IAM User Configuration
```bash
# Create IAM user with AdministratorAccess policy
# Configure AWS CLI
aws configure
```

#### 2. AWS ECR Repository
```bash
# Create ECR repository
aws ecr create-repository \
    --repository-name ragproj1 \
    --region your-region
```

### Environment Variables

Create the following GitHub Secrets:

| Secret Name | Description |
|-------------|-------------|
| `AWS_ACCESS_KEY_ID` | AWS IAM User Access Key |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM User Secret Key |
| `AWS_DEFAULT_REGION` | AWS Region (e.g., us-east-1) |
| `AWS_ECR_REPO_URI` | ECR Repository URI |

### Local Development

```bash
# Run the application locally
streamlit run app.py

# Build Docker image locally (optional)
docker build -t ragproj1 .
docker run -p 8501:8501 ragproj1
```

## 🔧 Technical Stack

### Core Technologies
- **Backend Framework**: Python 3.10+, LangChain
- **LLM Provider**: AWS Bedrock (Claude, Titan models)
- **Frontend**: Streamlit
- **Vector Database**: Integrated vector store for embeddings
- **Containerization**: Docker

### AWS Services
- **AWS Bedrock**: Large Language Model hosting
- **Amazon ECR**: Container registry
- **AWS App Runner**: Serverless container hosting
- **IAM**: Identity and access management

### DevOps & MLOps
- **CI/CD**: GitHub Actions
- **Infrastructure**: Docker containerization
- **Monitoring**: AWS CloudWatch (integrated with App Runner)
- **Version Control**: Git with automated workflows

## 📝 Usage

### Document Ingestion
1. Upload your documents through the Streamlit interface
2. The system will process and create vector embeddings
3. Documents are indexed for efficient retrieval

### Querying
1. Enter your question in natural language
2. The system retrieves relevant document chunks
3. LLM generates a comprehensive answer based on retrieved context

### Example Queries
- "What are the main conclusions of the quarterly report?"
- "Summarize the key risks mentioned in the document"
- "What are the recommended next steps?"

## 🔄 CI/CD Pipeline

The project includes a complete GitHub Actions workflow:

1. **Code Quality Checks**: Linting and formatting
2. **Testing**: Automated unit and integration tests
3. **Docker Build**: Container image creation
4. **ECR Push**: Automated deployment to AWS ECR
5. **App Runner Deploy**: Automatic service updates

## 📊 Monitoring & Observability

- **Application Logs**: Integrated logging throughout the application
- **Performance Metrics**: Response time and accuracy tracking
- **AWS CloudWatch**: Infrastructure monitoring
- **Error Tracking**: Comprehensive error handling and reporting

## 🛡️ Security Considerations

- **IAM Policies**: Principle of least privilege
- **API Security**: Secure endpoint configuration
- **Data Privacy**: Document processing with privacy controls
- **Access Control**: Role-based access management

## 🧪 Testing

```bash
# Run unit tests
python -m pytest tests/

# Run integration tests
python -m pytest tests/integration/

# Run linting
flake8 SRC/
black SRC/ --check
```

## 📈 Performance Optimization

- **Caching**: Intelligent caching of embeddings and responses
- **Parallel Processing**: Optimized document processing
- **Auto-scaling**: AWS App Runner automatic scaling
- **Resource Management**: Efficient memory and compute utilization

## 🔧 Troubleshooting

### Common Issues

1. **AWS Credentials**: Ensure proper IAM permissions
2. **Docker Build**: Check Dockerfile syntax and dependencies
3. **Memory Issues**: Monitor RAM usage during document processing
4. **API Limits**: Implement rate limiting for production use

### Debug Commands
```bash
# Check AWS configuration
aws sts get-caller-identity

# Test Docker build locally
docker build --no-cache -t ragproj1 .

# Check application logs
docker logs container_id
```

## 🗑️ Resource Cleanup

After testing or when decommissioning:

```bash
# Delete AWS resources
aws ecr delete-repository --repository-name ragproj1 --force
aws iam delete-user --user-name llmops-proj1
# Delete App Runner service through AWS Console
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] Multi-document type support (PDF, DOCX, TXT)
- [ ] Advanced RAG techniques (HyDE, ReACT)
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] API endpoint for programmatic access
- [ ] Integration with enterprise document systems

## 📞 Support

For questions or issues:
- 📧 Email: support@yourorganization.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/intelligent-rag-qa-system/issues)
- 📚 Documentation: [Project Wiki](https://github.com/yourusername/intelligent-rag-qa-system/wiki)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- AWS Bedrock team for LLM infrastructure
- LangChain community for the framework
- Streamlit for the amazing web framework
- Open source contributors

---

**Built with ❤️ for the future of document intelligence**
