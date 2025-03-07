package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  A container for all HandleRecords.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleRecordContainer  {

  private List<HandleAPIRecord> containsPids;

}
