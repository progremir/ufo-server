from rest_framework.response import Response
from rest_framework.views import APIView
from ufo.optimizers import DPKFlightOptimizer
from ufo.clients import KiwiClient


class FlightOptimizerView(APIView):
    def get(self, request):
        departure = request.query_params.get('from')
        destinations = request.query_params.getlist('to')
        try:
            optimizer = DPKFlightOptimizer(departure, destinations, KiwiClient)
            flight = optimizer.process()
        except Exception as e:
            return Response({'message': str(e)})

        return Response(
            {
                'destination': flight.destination.city.name,
                'dpk': flight.dpk,
            }
        )
