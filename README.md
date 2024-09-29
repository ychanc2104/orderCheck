# FastAPI Order Service


## SOLID 原則應用

### 1. 單一職責原則 (Single Responsibility Principle, SRP)

- **BaseService**：負責處理通用的請求流程，包括計時和生成回應。
- **CreateOrderService**：專注於訂單的創建和轉換邏輯。
- **OrderValidator**：專門處理訂單資料的驗證邏輯。
- **ResponseDto**：定義 固定的API 回應的資料結構。
- **OrderDto & AddressDto**：定義訂單和地址的資料傳輸物件。

### 2. 開放封閉原則 (Open/Closed Principle, OCP)

- **BaseService** 是一個抽象類別，允許通過繼承來擴展新服務，而不需要修改現有代碼。
- **CreateOrderService** 通過覆寫 `process_data` 方法來實現具體的訂單處理邏輯。
- **CurrencyConverterFactory** 透過 工廠模式 (Factory Pattern)，我們可以讓幣別轉換器的生成邏輯與具體的業務邏輯解耦，這樣在新增、修改幣別轉換邏輯時，只需要更新工廠類別中的選擇邏輯，而不需要修改服務層的代碼。這樣的設計方式符合 開放封閉原則 (OCP)，使系統更具擴展性，也使代碼的維護更加容易。
- 
### 3. 里氏替換原則 (Liskov Substitution Principle, LSP)

- 所有繼承自 `BaseService` 的類別（例如 `CreateOrderService`）都能夠替換 `BaseService`，且不會破壞程序的正確性。

### 4. 介面隔離原則 (Interface Segregation Principle, ISP)

- `BaseService` 提供了一個簡單的介面，僅包含必要的方法，避免客戶端依賴它們不需要的方法。

### 5. 依賴反轉原則 (Dependency Inversion Principle, DIP)

- 高層模組（如 `OrderTransformer`）依賴於抽象（`AbstractCurrencyConverter`），而非具體的實現類別（`CurrencyConverterFactory`）。

## 設計模式應用

### 策略模式 (Strategy Pattern)

- **OrderValidateWorker**：封裝了訂單的驗證邏輯，將每個驗證條件封裝成單獨的策略，這使得驗證邏輯變得更加靈活和可擴展。

### 工廠模式

- **CurrencyConverterFactory**：能產生各種幣別轉換成台幣的轉換器，未來有新需求時僅需新增新的轉換器與新增CurrencyConverterFactory中的case即可，無須修改上層程式碼。

## Translator
1. **使用gettext，方便指定管理各種拋錯，且未來可支援i18n**:

## How to Run

1. **Build Docker Image**:
   ```sh
   sudo docker-compose build
   ```

2. **Start Services**:
   ```sh
   sudo docker-compose up
   ```

## Endpoints

- `POST /api/orders/`: Create a new order.

## Swagger UI
   Go to `http://localhost:8000/docs` in your browser.
