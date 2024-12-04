import json
import uuid
import psycopg2
from psycopg2.extras import execute_values
from flask import Flask, jsonify, request
import os
from flask_cors import CORS

class PostgreSQLUploader:
    def __init__(self, db_url=None):
        """
        Initialize PostgreSQL connection
        
        Args:
            db_url (str): Database URL (e.g., postgres://user:password@host:port/dbname)
        """
        self.db_url = db_url or os.environ.get('DATABASE_URL')
        if not self.db_url:
            raise ValueError("Database URL must be provided either through constructor or DATABASE_URL environment variable")

    def connect(self):
        """Establish a database connection"""
        try:
            conn = psycopg2.connect(self.db_url)
            return conn
        except (Exception, psycopg2.Error) as error:
            print(f"Error connecting to PostgreSQL: {error}")
            raise
    
    def create_table(self):
        """Create careers table if not exists"""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS careers (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            domain VARCHAR(10) NOT NULL,
            role VARCHAR(100) NOT NULL,
            description TEXT,
            skills TEXT[],
            average_salary VARCHAR(20),
            growth_potential VARCHAR(20)
        )
        """
        conn = None
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(create_table_query)
            conn.commit()
            print("Table created successfully")
        except (Exception, psycopg2.Error) as error:
            print(f"Error creating table: {error}")
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def upload_careers(self, careers_file='mock_tech_careers.json'):
        """
        Upload careers from JSON file to PostgreSQL
        
        Args:
            careers_file (str): Path to JSON file with career data
        """
        # Read JSON file
        with open(careers_file, 'r') as f:
            career_data = json.load(f)
        
        # Prepare data for bulk insert
        careers_to_insert = []
        for domain, careers in career_data.items():
            for career in careers:
                careers_to_insert.append((
                    domain,
                    career['role'],
                    career.get('description', ''),
                    career.get('skills', []),
                    career.get('average_salary', ''),
                    career.get('growth_potential', '')
                ))
        
        # SQL insert query
        insert_query = """
        INSERT INTO careers 
        (domain, role, description, skills, average_salary, growth_potential) 
        VALUES %s
        """
        
        conn = None
        try:
            conn = self.connect()
            cursor = conn.cursor()
            
            # Clear existing data
            cursor.execute("DELETE FROM careers")
            
            # Bulk insert
            execute_values(cursor, insert_query, careers_to_insert)
            conn.commit()
            
            print(f"Uploaded {len(careers_to_insert)} careers")
            return len(careers_to_insert)
        
        except (Exception, psycopg2.Error) as error:
            print(f"Error uploading careers: {error}")
            if conn:
                conn.rollback()
            raise
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def fetch_careers(self):
        """Fetch all careers from the database"""
        conn = None
        try:
            conn = self.connect()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM careers")
            careers = cursor.fetchall()
            
            # Get column names
            column_names = [
                'id', 'domain', 'role', 'description', 
                'skills', 'average_salary', 'growth_potential'
            ]
            
            # Convert to list of dictionaries
            careers_list = [
                dict(zip(column_names, career)) for career in careers
            ]
            
            return careers_list
        
        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching careers: {error}")
            raise
        
        finally:
            if conn:
                cursor.close()
                conn.close()

# Flask App
app = Flask(__name__)
CORS(app)

# Initialize uploader (replace with your actual database URL)
uploader = PostgreSQLUploader("postgresql://careerdb_user:DjlIgxpBJTDNZmRL7YpD6o7Gq8hxtahn@dpg-ct6lodaj1k6c73ahheug-a.singapore-postgres.render.com/careerdb")

@app.route('/init_db', methods=['POST'])
def init_database():
    """Initialize database and create table"""
    try:
        uploader.create_table()
        return jsonify({
            'status': 'success',
            'message': 'Database initialized successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/upload_careers', methods=['POST'])
def upload_career_data():
    """Upload career data to database"""
    try:
        # Option to pass a different file via request
        careers_file = request.json.get('file', 'mock_tech_careers.json') if request.json else 'mock_tech_careers.json'
        
        count = uploader.upload_careers(careers_file)
        return jsonify({
            'status': 'success',
            'message': f'Uploaded {count} careers successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/careers', methods=['GET'])
def get_careers():
    """Retrieve all careers"""
    try:
        careers = uploader.fetch_careers()
        return jsonify({
            'status': 'success',
            'careers': careers,
            'total': len(careers)
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)
