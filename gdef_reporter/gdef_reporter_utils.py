from pathlib import Path

from gdef_reporter.gdef_reporter import GDEFContainerList, GDEFContainer, GDEFReporter


def create_gdef_reporter(gdf_path: Path, filter_dict: dict = None, use_gradient_plane: bool = False,
                         legendre_deg: int = 1, keep_offset: bool = False) -> GDEFReporter:
    gdf_container_list = GDEFContainerList()
    for gdf_file in gdf_path.glob("*.gdf"):
        gdf_container_list.append(GDEFContainer(gdf_file))
    gdf_container_list.correct_backgrounds(use_gradient_plane, legendre_deg, keep_offset)
    gdf_container_list.set_filter_ids(filter_dict)

    return GDEFReporter(gdf_container_list)
