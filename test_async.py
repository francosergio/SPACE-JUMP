import time
import asyncio

# --- ENFOQUE SÍNCRONO (Bloqueante) ---
def peticion_sincrona(usuario: int):
    print(f"[Sync] Usuario {usuario} inició petición.")
    time.sleep(2)  # Bloquea TODO el hilo de Python por 2 segundos
    print(f"[Sync] Usuario {usuario} terminó.")

def ejecutar_sync():
    inicio = time.time()
    peticion_sincrona(1)
    peticion_sincrona(2)
    print(f"⏱️ Tiempo total Síncrono: {time.time() - inicio:.2f} segundos\n")


# --- ENFOQUE ASÍNCRONO (No Bloqueante) ---
async def peticion_asincrona(usuario: int):
    print(f"[Async] Usuario {usuario} inició petición.")
    await asyncio.sleep(2)  # Libera el Event Loop durante estos 2 segundos
    print(f"[Async] Usuario {usuario} terminó.")

async def ejecutar_async():
    inicio = time.time()
    # Ejecutamos ambas peticiones en paralelo en el mismo Event Loop
    await asyncio.gather(
        peticion_asincrona(1),
        peticion_asincrona(2)
    )
    print(f"⏱️ Tiempo total Asíncrono: {time.time() - inicio:.2f} segundos")

if __name__ == "__main__":
    print("--- Ejecutando Síncrono ---")
    ejecutar_sync()

    print("--- Ejecutando Asíncrono ---")
    asyncio.run(ejecutar_async())
