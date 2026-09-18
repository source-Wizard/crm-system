# Deploying TechNova CRM to GitHub and Vercel Free Tier

This guide provides step-by-step instructions to upload your Django CRM project to GitHub and deploy it live on **Vercel** using their 100% free hobby tier.

---

## 1. Push to GitHub

### Step A: Create a New Repository on GitHub
1. Open your browser and go to [github.com/new](https://github.com/new).
2. Enter a repository name (e.g., `crm-system` or `technova-crm`).
3. Set the repository visibility to **Public** or **Private**.
4. **Important**: Leave "Add a README file", ".gitignore", and "Choose a license" **UNCHECKED** (we already have them configured).
5. Click **Create repository**.
6. Copy the repository URL (e.g., `https://github.com/<your-username>/crm-system.git`).

### Step B: Link & Push from Your Local Project
Open PowerShell or your terminal in this directory (`C:\Users\mohan\.gemini\antigravity\scratch\CRM_System`) and run:

```bash
# Add your GitHub repository as remote origin (replace with your actual GitHub URL)
git remote add origin https://github.com/<your-username>/crm-system.git

# Rename default branch to main
git branch -M main

# Push all files to GitHub
git push -u origin main
```

---

## 2. Set Up a 100% Free Cloud MySQL Database

Vercel functions are stateless and run in cloud servers, meaning they cannot connect to `127.0.0.1` on your local computer. You can use any free MySQL cloud provider. 

### Recommended: TiDB Cloud Serverless (Free Forever)
1. Go to [tidbcloud.com](https://tidbcloud.com) and sign up (free, no credit card required).
2. Create a free **Serverless** cluster (takes 10 seconds).
3. Under **Overview**, click **Connect** and select **Connect with General Client / Python**.
4. Note down your connection details:
   - `DB_HOST` (e.g., `gateway01.us-east-1.prod.aws.tidbcloud.com`)
   - `DB_PORT` (`4000` for TiDB or `3306`)
   - `DB_USER` (e.g., `xxxxxx.root`)
   - `DB_PASSWORD` (the password you created)
   - `DB_NAME` (`test` or create `crm_djangodb`)

*(Alternative: Aiven for MySQL Free Tier at [aiven.io](https://aiven.io) or Railway at [railway.app](https://railway.app))*

---

## 3. Deploy on Vercel Free Tier

### Step A: Import GitHub Repository to Vercel
1. Go to [vercel.com](https://vercel.com) and log in with your **GitHub account**.
2. From the Vercel Dashboard, click **Add New...** -> **Project**.
3. Locate your GitHub repository (`crm-system`) from the list and click **Import**.

### Step B: Configure Environment Variables in Vercel
Before clicking Deploy, expand **Environment Variables** in Vercel and add:

| Variable Name | Value | Description |
| :--- | :--- | :--- |
| `DB_HOST` | `gateway01.us-east-1.prod.aws.tidbcloud.com` | Your Cloud DB host |
| `DB_NAME` | `crm_djangodb` | Your Cloud DB name |
| `DB_USER` | `xxxx.root` | Your Cloud DB user |
| `DB_PASSWORD` | `your-db-password` | Your Cloud DB password |
| `DB_PORT` | `4000` (or `3306`) | Database port |
| `SECRET_KEY` | `your-secure-random-secret-key` | Django secret key |

*(Note: If you deploy without setting database variables first, the application will automatically fall back to preview mode with an ephemeral SQLite database so the build passes immediately).*

### Step C: Deploy
Click **Deploy**! Vercel will build the project, run `build_files.sh` to package static assets, and deploy the serverless Python WSGI handler.

Your CRM will be live at:
`https://<your-project-name>.vercel.app`

---

## 4. Default Login Credentials

Once deployed and migrated:
- **Super Admin**: `admin` / `Admin@123`
- **Manager**: `manager` / `Admin@123`
- **Sales Rep**: `sales` / `Admin@123`
- **Support Staff**: `support` / `Admin@123`
