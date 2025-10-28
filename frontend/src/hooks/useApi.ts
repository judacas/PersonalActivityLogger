import { useQuery, UseQueryResult } from '@tanstack/react-query'
import { apiClient } from '../services/api'

export function useApi<T>(endpoint: string): UseQueryResult<T, Error> {
  return useQuery({
    queryKey: [endpoint],
    queryFn: () => apiClient.get(endpoint),
  })
}

