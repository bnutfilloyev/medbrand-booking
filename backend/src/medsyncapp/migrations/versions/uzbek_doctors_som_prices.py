"""update doctors to uzbek names and som prices

Revision ID: uzbek_doctors_som_prices
Revises: 88bdd79e5a2f
Create Date: 2025-08-18 15:30:00.000000

"""
from typing import Sequence, Union
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'uzbek_doctors_som_prices'
down_revision: Union[str, None] = '88bdd79e5a2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Uzbek doctor names - mix of male and female names
uzbek_doctor_names = [
    "Dr. Akmal Karimov",
    "Dr. Gulnora Rashidova", 
    "Dr. Botir Nazarov",
    "Dr. Dilshoda Aripova",
    "Dr. Jamshid Tursunov",
    "Dr. Feruza Abdullayeva",
    "Dr. Sardor Umarov",
    "Dr. Nigora Saidova",
    "Dr. Ravshan Normatov",
    "Dr. Sevara Mirzayeva",
    "Dr. Ulugbek Yusupov",
    "Dr. Mavjuda Haydarova"
]


def upgrade() -> None:
    # Get the database connection
    conn = op.get_bind()
    
    # Get all doctors
    result = conn.execute(sa.text("SELECT doctor_id, price FROM doctors ORDER BY doctor_id"))
    doctors = result.fetchall()
    
    # Update each doctor with Uzbek name and convert price from USD to UZS
    # Approximate exchange rate: 1 USD = 12,300 UZS (as of 2025)
    usd_to_uzs_rate = 12300
    
    for i, (doctor_id, current_price_usd) in enumerate(doctors):
        # Use modulo to cycle through the names if there are more doctors than names
        uzbek_name = uzbek_doctor_names[i % len(uzbek_doctor_names)]
        
        # Convert price from USD to UZS and round to nearest thousand
        price_uzs = round(float(current_price_usd) * usd_to_uzs_rate, -3)  # Round to nearest 1000
        
        conn.execute(
            sa.text(
                "UPDATE doctors SET full_name = :full_name, price = :price WHERE doctor_id = :doctor_id"
            ),
            parameters=dict(
                full_name=uzbek_name,
                price=price_uzs,
                doctor_id=doctor_id
            )
        )
    
    # Also update diagnostic prices to UZS
    result = conn.execute(sa.text("SELECT diagnostic_id, price FROM diagnostics"))
    diagnostics = result.fetchall()
    
    for diagnostic_id, current_price_usd in diagnostics:
        # Convert diagnostic prices from USD to UZS
        price_uzs = round(float(current_price_usd) * usd_to_uzs_rate, -3)  # Round to nearest 1000
        
        conn.execute(
            sa.text(
                "UPDATE diagnostics SET price = :price WHERE diagnostic_id = :diagnostic_id"
            ),
            parameters=dict(
                price=price_uzs,
                diagnostic_id=diagnostic_id
            )
        )


def downgrade() -> None:
    # Get the database connection
    conn = op.get_bind()
    
    # Convert prices back from UZS to USD
    usd_to_uzs_rate = 12300
    
    # Revert doctor prices
    result = conn.execute(sa.text("SELECT doctor_id, price FROM doctors"))
    doctors = result.fetchall()
    
    for doctor_id, current_price_uzs in doctors:
        price_usd = round(float(current_price_uzs) / usd_to_uzs_rate, 2)
        
        conn.execute(
            sa.text(
                "UPDATE doctors SET price = :price WHERE doctor_id = :doctor_id"
            ),
            parameters=dict(
                price=price_usd,
                doctor_id=doctor_id
            )
        )
    
    # Revert diagnostic prices
    result = conn.execute(sa.text("SELECT diagnostic_id, price FROM diagnostics"))
    diagnostics = result.fetchall()
    
    for diagnostic_id, current_price_uzs in diagnostics:
        price_usd = round(float(current_price_uzs) / usd_to_uzs_rate, 2)
        
        conn.execute(
            sa.text(
                "UPDATE diagnostics SET price = :price WHERE diagnostic_id = :diagnostic_id"
            ),
            parameters=dict(
                price=price_usd,
                diagnostic_id=diagnostic_id
            )
        )
