import os
import re

posts_dir = r'c:\Users\NDK\Desktop\loading-blog\_posts'

def fix_posts():
    for filename in os.listdir(posts_dir):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. exp01~05 image paths
        content = content.replace("feature: '/img/posts/exp01/smainE.PNG'", "feature: '/img/post main bg.png'")
        content = content.replace("feature: '/img/posts/exp02/smainE.PNG'", "feature: '/img/post main bg.png'")
        content = content.replace("feature: '/img/posts/exp03/smainE.PNG'", "feature: '/img/post main bg.png'")
        content = content.replace("feature: '/img/posts/exp04/smainE.PNG'", "feature: '/img/post main bg.png'")
        content = content.replace("feature: '/img/posts/exp05/smainE.PNG'", "feature: '/img/post main bg.png'")
        
        content = content.replace("background: '/img/posts/exp01/bgimgexp.PNG'", "background: '/img/bg-experience.png'")
        content = content.replace("background: '/img/posts/exp02/bgimgexp.PNG'", "background: '/img/bg-experience.png'")
        content = content.replace("background: '/img/posts/exp03/bgimgexp.PNG'", "background: '/img/bg-experience.png'")
        content = content.replace("background: '/img/posts/exp04/bgimgexp.PNG'", "background: '/img/bg-experience.png'")
        content = content.replace("background: '/img/posts/exp05/bgimgexp.PNG'", "background: '/img/bg-experience.png'")
        
        # 2. info01~10 image paths
        content = re.sub(r"background: '/img/posts/info\d+/bgimginfo\.PNG'", "background: '/img/bg-information.png'", content)
        content = re.sub(r"feature: '/img/posts/info\d+/smainI\.PNG'", "feature: '/img/post main bg.png'", content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    fix_posts()
    print("Done")
