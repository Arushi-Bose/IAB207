from a3_group16 import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
    #disable debug mode once successfully deployed