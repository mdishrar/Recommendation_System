import random
import json
import uuid

def generate_additional_roles():
    additional_roles = {
        'CS': [
            {
                'role': 'Full Stack Developer',
                'description': 'Develop both client and server software for web applications.',
                'skills': ['JavaScript', 'React', 'Node.js', 'Backend Development'],
                'average_salary': '$115,000',
                'growth_potential': 'High'
            },
            {
                'role': 'Machine Learning Engineer',
                'description': 'Create and deploy advanced machine learning models and AI systems.',
                'skills': ['Deep Learning', 'TensorFlow', 'Python', 'Neural Networks'],
                'average_salary': '$135,000',
                'growth_potential': 'Excellent'
            },
            {
                'role': 'DevOps Engineer',
                'description': 'Manage infrastructure, continuous integration, and deployment processes.',
                'skills': ['Kubernetes', 'Docker', 'CI/CD', 'Cloud Platforms'],
                'average_salary': '$125,000',
                'growth_potential': 'Very High'
            },
            {
                'role': 'Blockchain Developer',
                'description': 'Design and implement blockchain-based solutions and smart contracts.',
                'skills': ['Solidity', 'Ethereum', 'Smart Contracts', 'Cryptography'],
                'average_salary': '$130,000',
                'growth_potential': 'High'
            },
            {
                'role': 'AR/VR Software Engineer',
                'description': 'Develop immersive augmented and virtual reality applications.',
                'skills': ['Unity', 'Unreal Engine', '3D Modeling', 'C#'],
                'average_salary': '$120,000',
                'growth_potential': 'Very High'
            }
        ],
        'IT': [
            {
                'role': 'Network Security Engineer',
                'description': 'Implement and maintain advanced network security protocols.',
                'skills': ['Firewall Management', 'Penetration Testing', 'Security Frameworks'],
                'average_salary': '$115,000',
                'growth_potential': 'Excellent'
            },
            {
                'role': 'Cloud Security Specialist',
                'description': 'Ensure security and compliance of cloud infrastructure.',
                'skills': ['Cloud Security', 'Compliance', 'Risk Management'],
                'average_salary': '$130,000',
                'growth_potential': 'Very High'
            },
            {
                'role': 'IT Infrastructure Manager',
                'description': 'Oversee and optimize organization\'s IT infrastructure and systems.',
                'skills': ['Systems Administration', 'Enterprise Architecture', 'Strategic Planning'],
                'average_salary': '$110,000',
                'growth_potential': 'High'
            },
            {
                'role': 'Cloud Support Engineer',
                'description': 'Provide technical support and troubleshooting for cloud services.',
                'skills': ['Technical Support', 'Cloud Platforms', 'Problem-Solving'],
                'average_salary': '$85,000',
                'growth_potential': 'Moderate'
            },
            {
                'role': 'AI Operations Specialist',
                'description': 'Manage and optimize AI and machine learning production environments.',
                'skills': ['MLOps', 'Cloud Computing', 'Model Deployment'],
                'average_salary': '$125,000',
                'growth_potential': 'High'
            }
        ],
        'ECE': [
            {
                'role': 'Robotics Engineer',
                'description': 'Design and develop advanced robotic systems and automation solutions.',
                'skills': ['Robot Programming', 'Mechanical Design', 'AI Integration'],
                'average_salary': '$110,000',
                'growth_potential': 'Excellent'
            },
            {
                'role': 'Semiconductor Design Engineer',
                'description': 'Create and optimize integrated circuit designs.',
                'skills': ['VLSI Design', 'Circuit Design', 'Hardware Description Languages'],
                'average_salary': '$120,000',
                'growth_potential': 'High'
            },
            {
                'role': '5G Network Engineer',
                'description': 'Design and implement next-generation wireless communication technologies.',
                'skills': ['Wireless Technologies', 'Network Architecture', 'Signal Processing'],
                'average_salary': '$115,000',
                'growth_potential': 'Very High'
            },
            {
                'role': 'Autonomous Systems Engineer',
                'description': 'Develop control systems for autonomous vehicles and drones.',
                'skills': ['Control Systems', 'Machine Learning', 'Sensor Fusion'],
                'average_salary': '$135,000',
                'growth_potential': 'Excellent'
            },
            {
                'role': 'Quantum Computing Research Engineer',
                'description': 'Explore and develop quantum computing technologies and algorithms.',
                'skills': ['Quantum Mechanics', 'Advanced Mathematics', 'Quantum Programming'],
                'average_salary': '$150,000',
                'growth_potential': 'Extremely High'
            }
        ]
    }
    return additional_roles

def generate_mock_careers(num_roles=500):
    base_data = {
        'CS': [
            {
                'role': 'Software Engineer',
                'description': 'Develop software applications and systems across various platforms.',
                'skills': ['Programming', 'Algorithm Design', 'Software Architecture'],
                'average_salary': '$110,000',
                'growth_potential': 'High'
            },
            {
                'role': 'Data Scientist',
                'description': 'Analyze complex data sets and develop machine learning models.',
                'skills': ['Machine Learning', 'Python', 'Statistical Analysis'],
                'average_salary': '$125,000',
                'growth_potential': 'Very High'
            },
            {
                'role': 'Cloud Solutions Architect',
                'description': 'Design and implement cloud computing strategies for organizations.',
                'skills': ['AWS', 'Azure', 'Cloud Security'],
                'average_salary': '$140,000',
                'growth_potential': 'Excellent'
            }
        ],
        'IT': [
            {
                'role': 'Cybersecurity Analyst',
                'description': 'Protect organizational networks and systems from cyber threats.',
                'skills': ['Network Security', 'Threat Detection', 'Incident Response'],
                'average_salary': '$105,000',
                'growth_potential': 'High'
            },
            {
                'role': 'IT Support Specialist',
                'description': 'Provide technical support and maintain computer systems.',
                'skills': ['Troubleshooting', 'Network Management', 'Customer Service'],
                'average_salary': '$55,000',
                'growth_potential': 'Moderate'
            },
            {
                'role': 'Cloud Engineer',
                'description': 'Manage and optimize cloud infrastructure and services.',
                'skills': ['Cloud Platforms', 'Containerization', 'DevOps'],
                'average_salary': '$120,000',
                'growth_potential': 'Excellent'
            }
        ],
        'ECE': [
            {
                'role': 'Embedded Systems Engineer',
                'description': 'Design and develop embedded software and hardware solutions.',
                'skills': ['C/C++', 'Microcontrollers', 'Hardware Design'],
                'average_salary': '$95,000',
                'growth_potential': 'High'
            },
            {
                'role': 'Telecommunications Engineer',
                'description': 'Design and maintain communication networks and systems.',
                'skills': ['Network Design', 'Signal Processing', 'Wireless Technologies'],
                'average_salary': '$90,000',
                'growth_potential': 'Moderate'
            },
            {
                'role': 'IoT Solutions Architect',
                'description': 'Create innovative Internet of Things (IoT) solutions.',
                'skills': ['Sensor Networks', 'Wireless Communication', 'Cloud Integration'],
                'average_salary': '$130,000',
                'growth_potential': 'Very High'
            }
        ]
    }
    
    # Add additional roles
    additional_roles = generate_additional_roles()
    for domain in base_data.keys():
        base_data[domain].extend(additional_roles[domain])
    
    mock_careers = {
        'CS': [],
        'IT': [],
        'ECE': []
    }
    
    # Generate variations of existing roles
    for domain, roles in base_data.items():
        while len(mock_careers[domain]) < num_roles // 3:
            base_role = random.choice(roles)
            
            # Create a variation of the role
            variations = [
                f'Senior {base_role["role"]}',
                f'Lead {base_role["role"]}',
                f'Principal {base_role["role"]}',
                f'Staff {base_role["role"]}',
                f'Advanced {base_role["role"]}',
            ]
            
            variation_role = base_role.copy()
            variation_role['role'] = random.choice(variations)
            
            # Adjust salary based on variation
            current_salary = int(variation_role['average_salary'].replace('$', '').replace(',', ''))
            variation_role['average_salary'] = f'${current_salary + random.randint(10000, 40000):,}'
            
            # Add unique identifier
            variation_role['id'] = str(uuid.uuid4())
            
            # Potentially add more skills or modify existing
            if random.random() < 0.3:
                variation_role['skills'].append(random.choice([
                    'Project Management', 'Team Leadership', 'Strategic Planning', 
                    'Enterprise Architecture', 'Technical Mentoring'
                ]))
            
            # Adjust growth potential slightly
            potential_options = ['Moderate', 'High', 'Very High', 'Excellent']
            variation_role['growth_potential'] = random.choice(potential_options)
            
            mock_careers[domain].append(variation_role)
    
    return mock_careers

# Generate and save mock careers
mock_careers = generate_mock_careers()

# Optional: Save to JSON file
with open('mock_tech_careers.json', 'w') as f:
    json.dump(mock_careers, f, indent=2)

# Print summary
for domain, careers in mock_careers.items():
    print(f"{domain} Careers: {len(careers)} roles")

# Return the mock careers
mock_careers