from schemas import MusicInfoSchema, MusicDifficultySchema, ChartDataSchema
from sa.engine import DatabaseEngine
from sa.tables import ChunithmMusic, ChunithmMusicDifficulty, ChunithmChartData


async def get_all_chunithm_music_data(
    engine: DatabaseEngine,
) -> tuple[list[MusicInfoSchema], list[MusicDifficultySchema], list[ChartDataSchema]]:
    music = await engine.select(ChunithmMusic)
    music_difficulties = await engine.select(ChunithmMusicDifficulty)
    chart_data = await engine.select(ChunithmChartData)
    return (
        [MusicInfoSchema.model_validate(m) for m in music],
        [MusicDifficultySchema.model_validate(m) for m in music_difficulties],
        [ChartDataSchema.model_validate(m) for m in chart_data],
    )
