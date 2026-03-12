# Memory Palace Deployment Guide

**Status**: Ready to deploy to Coolify  
**Repo**: https://github.com/theharkco/memory-palace

---

## 🚀 Quick Deploy (Recommended)

### Via Coolify UI (easiest):

1. Go to **https://apps.harkco.se**
2. Click **"Create New Resource"**
3. Select **"GitHub"** as the source
4. Choose **"Public repository"** option
5. Enter repository URL: `https://github.com/theharkco/memory-palace`
6. Git branch: `main`
7. **Build Pack**: Select **"Dockerfile"** (not Nixpacks!)
8. **Port**: `8501`
9. **Start Command**: `streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0`
10. **Custom Domain** (optional): `memory-palace.apps.harkco.se`
11. Enable **"Auto Deploy"** for automatic CI/CD
12. Click **"Create"**

### Expected Deployment URL:
After successful deployment: **https://memory-palace.apps.harkco.se**

---

## ⚙️ Configuration Details

| Setting | Value |
|---------|-------|
| **Build Pack** | Dockerfile |
| **Port** | 8501 |
| **Start Command** | `streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0` |
| **Python Version** | 3.11 (from Dockerfile) |

---

## 📦 Dockerfile Overview

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
EXPOSE 8501
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🔧 Alternative: Deploy via API

If you have the Coolify project/server UUIDs:

```bash
# Get token from 1Password vault "minihark" → "Coolify API Token"
TOKEN=$(op read "op://minihark/Coolify API Token/notesPlain")

# Create application
curl -X POST https://apps.harkco.se/api/v1/applications \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "project_uuid": "YOUR_PROJECT_UUID",
    "server_uuid": "YOUR_SERVER_UUID",
    "name": "memory-palace",
    "git_repository": "https://github.com/theharkco/memory-palace",
    "git_branch": "main",
    "build_pack": "dockerfile",
    "ports": "8501:8501",
    "start_command": "streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0",
    "domains": "memory-palace.apps.harkco.se"
  }'
```

---

## 🎯 What Memory Palace Does

The **Method of Loci** is an ancient Greek mnemonic technique that uses spatial memory to improve recall. This app lets you:

- Create virtual "rooms" as memory spaces
- Place "memory objects" with descriptions and precise locations
- Track your progress with a stats dashboard
- Organize information spatially for better learning

Perfect for studying, preparing presentations, or training your memory!

---

**Built**: 2026-03-12  
**Stack**: Python 3.11 + Streamlit + Docker