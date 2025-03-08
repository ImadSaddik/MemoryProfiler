from memory_profiler import profile
from langchain_community.document_loaders import UnstructuredExcelLoader


@profile
def extract_content_from_excel_file(file_path: str) -> str:
    loader = UnstructuredExcelLoader(file_path)
    documents = loader.load()
    file_content = ""
    for doc in documents:
        file_content += doc.page_content + "\n"

    return file_content.strip()


if __name__ == "__main__":
    file_path = "./data.xlsx"
    content = extract_content_from_excel_file(file_path)
    print(len(content))
