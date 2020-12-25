class Message:
    @staticmethod
    def content_not_found():
        return {
            "services": [],
            "message": "No services found under this identifier. Check the docs at https://github.com/mervin16/Mauritius-Emergency-Services-Api",
            "success": False,
        }

    @staticmethod
    def content_bad_request():
        return {
            "services": [],
            "message": "Your browser sent a request that this server could not understand. Check the docs at https://github.com/mervin16/Mauritius-Emergency-Services-Api",
            "success": False,
        }

    @staticmethod
    def content_service(service):
        return {
            "services": [service],
            "message": "",
            "success": True,
        }

    @staticmethod
    def content_services(services):
        return {"services": services, "message": "", "success": True}
