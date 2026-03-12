# 🏛️ Memory Palace - Deployment Instructions

**Repo**: https://github.com/theharkco/memory-palace

---

## 🚀 Deploy via Coolify UI (Fastest)

1. Visit **https://apps.harkco.se**
2. Click **"Create New Resource"**
3. Select **"GitHub"** → Choose **"Public repository"**
4. Repository: `https://github.com/theharkco/memory-palace`
5. **Build Pack**: `Dockerfile` (⚠️ NOT Nixpacks!)
6. **Port**: `8501`
7. **Start Command**: 
   ```
   streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0
   ```
8. **Domain** (optional): `memory-palace.apps.harkco.se`
9. ✅ Enable Auto Deploy
10. Click **Create**

---

## ✅ What's Ready

- ✅ App built with Python 3.11 + Streamlit
- ✅ Tested locally successfully
- ✅ Code pushed to GitHub
- ✅ Dockerfile configured
- ✅ Deployment guide in repo

---

## 🌐 Expected URL

After deployment: **https://memory-palace.apps.harkco.se**

---

*Status: Ready to deploy! 🏛️*