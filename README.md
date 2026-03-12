# 🏛️ Memory Palace Builder

**Memory Palace Builder** - A visual memory aid application using the ancient **Method of Loci** technique.

## 🎯 Concept

The Method of Loci is a mnemonic device dating back to ancient Greece and Rome. It involves mentally placing items you want to remember in specific locations within a familiar spatial environment (a "palace" or room). Studies show this technique can significantly improve memory retention and recall.

This app helps you:
- Create virtual "rooms" as memory spaces
- Place "memory objects" (items to remember) in specific locations
- Organize information spatially for better recall
- Build personalized memory palaces for studying, presentations, or learning

## 🛠️ Tech Stack

- **Python 3.11** (Slim base image)
- **Streamlit** for beautiful interactive UI
- **Local Storage** (session-based persistence)
- **CSS Gradients** for atmospheric design

## 🎨 Features

- **Room Management**: Create, view, and delete rooms for your memory palace
- **Memory Objects**: Add items with descriptions and precise placement locations
- **Visual Organization**: Browse all rooms and their contents
- **Beautiful UI**: Purple gradient aesthetic with smooth animations
- **Stats Dashboard**: Track your palace's progress
- **Responsive Design**: Works on desktop and mobile

## 📁 Project Structure

```
memory-palace/
├── src/
│   └── app.py          # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
└── README.md          # This file
```

## 🚀 Deployment

### Local Testing
```bash
pip install -r requirements.txt
streamlit run src/app.py
```

### Coolify Deployment
- **Repository**: `https://github.com/theharkco/memory-palace`
- **Build Pack**: Dockerfile
- **Port**: 8501
- **Start Command**: `streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0`

### Via Coolify API
```bash
# Create application
curl -X POST https://apps.harkco.se/api/v1/applications \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "project_uuid": "YOUR_PROJECT_UUID",
    "server_uuid": "YOUR_SERVER_UUID",
    "name": "memory-palace",
    "git_repository": "https://github.com/theharkco/memory-palace",
    "git_branch": "main",
    "docker_registry_image": "",
    "build_pack": "dockerfile",
    "ports": "8501:8501"
  }'
```

## 📝 Usage Tips

1. **Start with Familiar Spaces**: Use real places you know (your home, workplace, school)
2. **Be Specific**: The more detailed the placement ("on the red velvet chair by the window" vs "in the living room"), the better the recall
3. **Create Associations**: Add vivid descriptions to each memory object
4. **Use Multiple Rooms**: Organize by topic, date, or category
5. **Review Regularly**: Mentally "walk through" your palace to reinforce memories

## 🌐 Live URL

After deployment: `https://memory-palace.apps.harkco.se`

---

*Built on 2026-03-12 with Python & Streamlit! 🏛️*