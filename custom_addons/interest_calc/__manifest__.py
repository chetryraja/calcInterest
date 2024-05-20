{
    "name": "Interest Calculation",
    "version": "1.0",
    "category": "Tools",
    "sequence": -250,
    "summary": "Simple and compound interest calculator",
    "description": """
        Simple and Compund Interest Calculation
    """,
    "author": "Amicure Health",
    "website": "http://www.example.com",
    "license": "LGPL-3",
    "depends": ["base", "web"],
    "data": [
        "views/view.xml",
        "security/ir.model.access.csv",
        "report/interest_calc_report.xml",
        "report/interest_calculation_menu.xml",
        "report/interest_calculation_report_template.xml",
       
        
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
