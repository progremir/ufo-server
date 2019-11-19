from rest_framework.response import Response
from rest_framework.views import APIView
from ufo.optimizers import DPKFlightOptimizer
from ufo.clients import KiwiClient


class FlightOptimizerView(APIView):
    def get(self, request):
        departure = request.query_params.get('from')
        destinations = request.query_params.getlist('to')
        optimizer = DPKFlightOptimizer(departure, destinations, KiwiClient)
        flight = optimizer.process()
        return Response(
            {
                'destination': flight.destination.city.name,
                'dpk': flight.dpk,
            }
        )
