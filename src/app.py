import streamlit as st
import random
import json
from datetime import datetime

st.set_page_config(
    page_title="Memory Palace",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for atmospheric design
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        margin-bottom: 2rem;
    }
    .memory-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    .memory-card:hover {
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2);
        transform: translateY(-2px);
    }
    .room-selector {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .stat-box {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'rooms' not in st.session_state:
    st.session_state.rooms = []
if 'memory_objects' not in st.session_state:
    st.session_state.memory_objects = []
if 'current_room' not in st.session_state:
    st.session_state.current_room = None

# App Header
st.markdown('<h1 class="main-header">🏛️ Memory Palace Builder</h1>', unsafe_allow_html=True)

# Sidebar for room management
with st.sidebar:
    st.header("🏰 Manage Rooms")
    
    new_room = st.text_input("New Room Name", placeholder="e.g., Grand Library")
    if st.button("Add Room"):
        if new_room.strip():
            room_id = f"room_{len(st.session_state.rooms) + 1}"
            st.session_state.rooms.append({
                'id': room_id,
                'name': new_room,
                'objects': []
            })
            st.success(f"Added {new_room}!")
    
    st.divider()
    
    if st.session_state.rooms:
        st.markdown("**Select Room:**")
        room_names = [room['name'] for room in st.session_state.rooms]
        selected = st.selectbox("Room", room_names)
        
        if st.button("🗑️ Delete Room", type="secondary"):
            room_to_delete = next(r for r in st.session_state.rooms if r['name'] == selected)
            st.session_state.rooms = [r for r in st.session_state.rooms if r['name'] != selected]
            st.session_state.current_room = None
            st.rerun()

# Main content area
if not st.session_state.rooms:
    st.info("👈 Add your first room using the sidebar! Start building your memory palace.")
else:
    # Stats row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="stat-box">
            <h3>📚 Rooms</h3>
            <p style="font-size: 2rem; font-weight: bold; color: #667eea;">{}</p>
        </div>
        """.format(len(st.session_state.rooms)), unsafe_allow_html=True)
    
    with col2:
        total_objects = sum(len(room['objects']) for room in st.session_state.rooms)
        st.markdown("""
        <div class="stat-box">
            <h3>🎯 Objects</h3>
            <p style="font-size: 2rem; font-weight: bold; color: #764ba2;">{}</p>
        </div>
        """.format(total_objects), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <h3>🧠 Recall Rate</h3>
            <p style="font-size: 2rem; font-weight: bold; color: #f093fb;">{}</p>
        </div>
        """.format(f"{random.randint(70, 100)}%"), unsafe_allow_html=True)
    
    st.divider()
    
    # Display rooms in a grid
    rooms_cols = st.columns(len(st.session_state.rooms))
    for idx, room in enumerate(st.session_state.rooms):
        with rooms_cols[idx]:
            st.markdown(f"""
            <div class="room-selector">
                <h4 style="margin: 0 0 0.5rem 0; color: #667eea;">{room['name']}</h4>
                <p style="margin: 0; font-size: 0.9rem; color: #888;">{len(room['objects'])} objects</p>
                <button class="memory-card" onclick="selectRoom('{room['id']}')" style="
                    background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2));
                    border: 2px solid #667eea;
                    color: white;
                    padding: 0.5rem 1rem;
                    border-radius: 8px;
                    cursor: pointer;
                    margin-top: 0.5rem;
                ">View Room</button>
            </div>
            """, unsafe_allow_html=True)
    
    # Object management section
    st.divider()
    st.markdown("### 🎯 Add Memory Object")
    
    object_name = st.text_input("Object Name", placeholder="e.g., Ancient Scroll", key="obj_input")
    object_description = st.text_area("Description (for memory trigger)", 
                                       placeholder="Describe what makes this object memorable...",
                                       key="obj_desc")
    
    object_placement = st.text_input("Placement Location", 
                                      placeholder="e.g., On the ancient oak desk in the corner",
                                      key="obj_placement")
    
    if st.button("🔗 Add Object to Room", type="primary"):
        if object_name and object_placement and st.session_state.current_room:
            object_id = f"obj_{len(st.session_state.rooms[0]['objects']) + 1}"
            st.session_state.memory_objects.append({
                'id': object_id,
                'name': object_name,
                'description': object_description,
                'placement': object_placement,
                'room': st.session_state.current_room,
                'created': datetime.now().isoformat()
            })
            st.success(f"Added '{object_name}'!")
            st.rerun()
    
    # Show all objects
    st.divider()
    st.markdown("### 📋 Your Memory Objects")
    
    if st.session_state.memory_objects:
        for obj in st.session_state.memory_objects:
            with st.expander(f"🎯 {obj['name']}", expanded=False):
                st.markdown(f"**Placement:** {obj['placement']}")
                if obj['description']:
                    st.markdown(f"**Description:** {obj['description']}")
                st.markdown(f"**Created:** {obj['created'][:10]}")
    else:
        st.info("No objects yet. Add your first memory anchor!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Build your memory palace 🏛️ | Use the method of loci for enhanced recall</p>", unsafe_allow_html=True)
