package None;

import java.util.List;
import lombok.*;






/**
  The data element in the handle API for the landing page URL.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class URL extends HandleRecord {

  private int index;
  private HdlDataUrl data;

}
