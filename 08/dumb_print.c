/* head fileのインクルード */
#include <Python.h>

/* Python で dumb_print.print() すると起動される関数 */
static PyObject *
dumb_print(PyObject *self, PyObject *args) {
        /* unicode文字列をUTF-iエンコーディングのchar文字列に変換する */
	const char *text;
	if (!PyArg_ParseTuple(args, "s", &text))
		return NULL;
        /* char文字列の出力 */
	printf("%s\n", text);
        /* 戻り値の指定：ここではなし */
	Py_RETURN_NONE;
        /* 読み替えると以下
	   Py_INCREF(Py_Node);
	   return Py_None;  */
}

/* 拡張モジュールで提供する関数のリスト */
static PyMethodDef dumb_print_methods[] = {
	{"print", dumb_print, METH_VARARGS, "Print text"},
        /* sentinel リストの終わりを示すものかな？ */
	{NULL, NULL, 0, NULL}
};

/* 拡張モジュールのデータを登録する構造体:PyModuleDef */
static struct PyModuleDef dumb_print_module = {
	PyModuleDef_HEAD_INIT,
        /* モジュール名 */
	"dumb_print",
        /* どきゅめんてーしょんもじれつ */
	"sample extension module",
        /* Pythonインタプリタで管理するモジュール固有データのサイズ。独自にグローバル変数で管理する場合は-1 */
	-1,
        /* PyMethodDefへのポインタ */
	dumb_print_methods
};

/* ライブラリのロード＆初期化 PyInit_HOGEHOGE */
PyMODINIT_FUNC
PyInit_dumb_print(void) {
	return PyModule_Create(&dumb_print_module);
}
